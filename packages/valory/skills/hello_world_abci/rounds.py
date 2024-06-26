# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2023 Valory AG
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""This module contains the data classes for the Hello World ABCI application."""

from abc import ABC
from enum import Enum
from typing import Dict, List, Optional, Set, Tuple, Type, cast

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
    BaseSynchronizedData,
    CollectDifferentUntilAllRound,
    CollectSameUntilAllRound,
    CollectSameUntilThresholdRound,
    CollectionRound,
    DeserializedCollection,
    get_name,
)
from packages.valory.skills.hello_world_abci.payloads import (
    CollectRandomnessPayload,
    PrintMessagePayload,
    PrintCountPayload,
    RegistrationPayload,
    ResetPayload,
    SelectKeeperPayload,
)


class Event(Enum):
    """Event enumeration for the Hello World ABCI demo."""

    DONE = "done"
    ROUND_TIMEOUT = "round_timeout"
    NO_MAJORITY = "no_majority"
    RESET_TIMEOUT = "reset_timeout"


class SynchronizedData(
    BaseSynchronizedData
):  # pylint: disable=too-many-instance-attributes
    """
    Class to represent the synchronized data.

    This state is replicated by the Tendermint application.
    """

    @property
    def print_count(self) -> int:
        """Get the print count."""
        return cast(int, self.db.get("print_count", 0))

    @property
    def printed_messages(self) -> List[str]:
        """Get the printed messages list."""

        return cast(
            List[str],
            self.db.get_strict("printed_messages"),
        )
    
    @property
    def print_count_payloads(self) -> DeserializedCollection:
        """Retrieve the mapping of agent addresses to their print count payloads."""
        serialized = self.db.get("print_count_payloads", "{}")
        deserialized = CollectionRound.deserialize_collection(serialized)
        return cast(DeserializedCollection, deserialized)


class HelloWorldABCIAbstractRound(AbstractRound, ABC):
    """Abstract round for the Hello World ABCI skill."""

    synchronized_data_class: Type[BaseSynchronizedData] = SynchronizedData

    @property
    def synchronized_data(self) -> SynchronizedData:
        """Return the synchronized data."""
        return cast(SynchronizedData, self._synchronized_data)


class RegistrationRound(CollectSameUntilAllRound, HelloWorldABCIAbstractRound):
    """A round in which the agents get registered"""

    payload_class = RegistrationPayload

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Event]]:
        """Process the end of the block."""

        if self.collection_threshold_reached:
            synchronized_data = self.synchronized_data.update(
                participants=tuple(sorted(self.collection)),
                synchronized_data_class=SynchronizedData,
            )
            return synchronized_data, Event.DONE
        return None


class CollectRandomnessRound(
    CollectSameUntilThresholdRound, HelloWorldABCIAbstractRound
):
    """A round for collecting randomness"""

    payload_class = CollectRandomnessPayload
    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    no_majority_event = Event.NO_MAJORITY
    collection_key = get_name(SynchronizedData.participant_to_randomness)
    selection_key = get_name(SynchronizedData.most_voted_randomness)


class SelectKeeperRound(CollectSameUntilThresholdRound, HelloWorldABCIAbstractRound):
    """A round in a which keeper is selected"""

    payload_class = SelectKeeperPayload
    synchronized_data_class = SynchronizedData
    done_event = Event.DONE
    no_majority_event = Event.NO_MAJORITY
    collection_key = get_name(SynchronizedData.participant_to_selection)
    selection_key = get_name(SynchronizedData.most_voted_keeper_address)


class PrintMessageRound(CollectDifferentUntilAllRound, HelloWorldABCIAbstractRound):
    """A round in which the keeper prints the message"""

    payload_class = PrintMessagePayload

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Event]]:
        """Process the end of the block."""
        if self.collection_threshold_reached:
            synchronized_data = self.synchronized_data.update(
                participants=tuple(sorted(self.collection)),
                printed_messages=sorted(
                    [
                        cast(PrintMessagePayload, payload).message
                        for payload in self.collection.values()
                    ]
                ),
                synchronized_data_class=SynchronizedData,
            )
            return synchronized_data, Event.DONE
        return None


class PrintCountRound(CollectSameUntilThresholdRound, HelloWorldABCIAbstractRound):
    """A round for handling the PrintCountPayload."""

    payload_class = PrintCountPayload
    done_event = Event.DONE
    no_majority_event = Event.NO_MAJORITY
    collection_key = get_name(SynchronizedData.print_count_payloads)
    selection_key = get_name(SynchronizedData.print_count)

    def end_block(self) -> Optional[Tuple[SynchronizedData, Event]]:
        """Process the end of the block."""

        # First, check if the threshold has been reached and if there is a most voted payload
        if self.threshold_reached:
            if any(val is not None for val in self.most_voted_payload_values(self.selection_key)):
                # Get the most voted payload's print count
                most_voted_payload = self.get_most_voted_payload(self.selection_key)
                most_voted_print_count = most_voted_payload.print_count

                # Update the synchronized data with the most voted print count
                synchronized_data = self.synchronized_data.update(
                    synchronized_data_class=SynchronizedData,
                    **{self.selection_key: most_voted_print_count}
                )
                return synchronized_data, self.done_event
            else:
                # No valid majority found, return NONE event
                return None

        # Check if a majority is still possible
        if not self.is_majority_possible(self.collection_key, self.synchronized_data.nb_participants):
            return self.synchronized_data, self.no_majority_event

        return None


class ResetAndPauseRound(CollectSameUntilThresholdRound, HelloWorldABCIAbstractRound):
    """This class represents the base reset round."""

    payload_class = ResetPayload

    def end_block(self) -> Optional[Tuple[BaseSynchronizedData, Event]]:
        """Process the end of the block."""
        if self.threshold_reached:
            return self.synchronized_data.create(), Event.DONE
        if not self.is_majority_possible(
            self.collection, self.synchronized_data.nb_participants
        ):
            return self.synchronized_data, Event.NO_MAJORITY
        return None


class HelloWorldAbciApp(AbciApp[Event]):
    """HelloWorldAbciApp

    Initial round: RegistrationRound

    Initial states: {RegistrationRound}

    Transition states:
        0. RegistrationRound
            - done: 1.
        1. CollectRandomnessRound
            - done: 2.
            - no majority: 1.
            - round timeout: 1.
        2. SelectKeeperRound
            - done: 3.
            - no majority: 0.
            - round timeout: 0.
        3. PrintMessageRound
            - done: 4.
            - round timeout: 0.
        4. PrintCountRound
            - done: 5.
            - no majority: 0.
            - reset timeout: 0.
        5. ResetAndPauseRound
            - done: 1.
            - no majority: 0.
            - reset timeout: 0.

    Final states: {}

    Timeouts:
        round timeout: 30.0
        reset timeout: 30.0
    """

    initial_round_cls: AppState = RegistrationRound
    transition_function: AbciAppTransitionFunction = {
        RegistrationRound: {
            Event.DONE: CollectRandomnessRound,
        },
        CollectRandomnessRound: {
            Event.DONE: SelectKeeperRound,
            Event.NO_MAJORITY: CollectRandomnessRound,
            Event.ROUND_TIMEOUT: CollectRandomnessRound,
        },
        SelectKeeperRound: {
            Event.DONE: PrintMessageRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.ROUND_TIMEOUT: RegistrationRound,
        },
        PrintMessageRound: {
            Event.DONE: PrintCountRound,
            Event.ROUND_TIMEOUT: RegistrationRound,
        },
        PrintCountRound: {
            Event.DONE: ResetAndPauseRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.ROUND_TIMEOUT: RegistrationRound,
        },
        ResetAndPauseRound: {
            Event.DONE: CollectRandomnessRound,
            Event.NO_MAJORITY: RegistrationRound,
            Event.RESET_TIMEOUT: RegistrationRound,
        },
    }
    event_to_timeout: Dict[Event, float] = {
        Event.ROUND_TIMEOUT: 30.0,
        Event.RESET_TIMEOUT: 30.0,
    }
    cross_period_persisted_keys: Set[str] = {
        get_name(SynchronizedData.print_count),
    }
