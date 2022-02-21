# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2021-2022 Valory AG
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

"""This module contains the data classes for the reset_pause_abci application."""
from abc import ABC
from enum import Enum
from typing import Dict, Optional, Set, Tuple, Type, cast

from packages.valory.skills.abstract_round_abci.base import (
    AbciApp,
    AbciAppTransitionFunction,
    AbstractRound,
    AppState,
)
from packages.valory.skills.abstract_round_abci.base import (
    BasePeriodState as PeriodState,
)
from packages.valory.skills.abstract_round_abci.base import (
    CollectSameUntilThresholdRound,
    DegenerateRound,
)
from packages.valory.skills.reset_pause_abci.payloads import (
    ResetPayload,
    TransactionType,
)


class Event(Enum):
    """Event enumeration for the reset_pause_abci app."""

    DONE = "done"
    ROUND_TIMEOUT = "round_timeout"
    NO_MAJORITY = "no_majority"
    RESET_TIMEOUT = "reset_timeout"


class ResetPauseABCIAbstractRound(AbstractRound[Event, TransactionType], ABC):
    """Abstract round for the reset_pause_abci skill."""

    @property
    def period_state(self) -> PeriodState:
        """Return the period state."""
        return cast(PeriodState, self._state)

    def _return_no_majority_event(self) -> Tuple[PeriodState, Event]:
        """
        Trigger the NO_MAJORITY event.

        :return: a new period state and a NO_MAJORITY event
        """
        return self.period_state, Event.NO_MAJORITY


class ResetAndPauseRound(CollectSameUntilThresholdRound, ResetPauseABCIAbstractRound):
    """A round representing that consensus was reached (the final round)."""

    allowed_tx_type = ResetPayload.transaction_type
    payload_attribute = "period_count"
    round_id = "reset_and_pause"

    def end_block(self) -> Optional[Tuple[PeriodState, Event]]:
        """Process the end of the block."""
        if self.threshold_reached:
            state = self.period_state.update(
                period_count=self.most_voted_payload,
                participants=self.period_state.participants,
            )
            return state, Event.DONE
        if not self.is_majority_possible(
            self.collection, self.period_state.nb_participants
        ):
            return self._return_no_majority_event()
        return None


class FinishedResetAndPauseRound(DegenerateRound):
    """A round that represents swap back has finished"""

    round_id = "finished_reset_pause"


class ResetPauseABCIApp(AbciApp[Event]):
    """ResetPauseABCIApp

    Initial round: RegistrationRound

    Initial states: {RegistrationRound}

    Transition states:

    0. ResetAndPauseRound
        - done: 1.
        - reset timeout: 0.
        - no majority: 0.
    1. FinishedResetAndPauseRound

    Final states: {
        FinishedResetAndPauseRound,
    }

    Timeouts:
        round timeout: 30.0
        reset timeout: 30.0
    """

    initial_round_cls: Type[AbstractRound] = ResetAndPauseRound
    transition_function: AbciAppTransitionFunction = {
        ResetAndPauseRound: {
            Event.DONE: FinishedResetAndPauseRound,
            Event.RESET_TIMEOUT: ResetAndPauseRound,
            Event.NO_MAJORITY: ResetAndPauseRound,
        },
        FinishedResetAndPauseRound: {},
    }
    final_states: Set[AppState] = {
        FinishedResetAndPauseRound,
    }
    event_to_timeout: Dict[Event, float] = {
        Event.ROUND_TIMEOUT: 30.0,
        Event.RESET_TIMEOUT: 30.0,
    }
