# Finite State Machine

<!-- [![Latest Release](https://img.shields.io/pypi/v/finite-state-machine)]() -->
[![Version](https://img.shields.io/badge/version-v0.1.0-orange.svg)](https://github.com/dralm3ida/finite-state-machine)
[![Supports Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/download/releases/)
[![License](https://img.shields.io/github/license/dralm3ida/finite-state-machine.svg)](LICENSE)

Object-oriented finite state machine implementation using python

#### Table of Contents

<!-- TOC -->

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

<!-- /TOC -->

## Installation

Download source code and run the following commands to install and uninstall the package:
```console
pip install .
pip uninstall fsm_finite_state_machine
```

## Usage
There are 3 main classes in this package to be used:
1. `State` - Contains the definition of the state machine state as a string key
2. `Transition` - Contains the definition of a state machine transition, such as transition name, the source state and the destination state
3. `FSM` - Is the definition of the Finite State Machine which must be instatiated with the following arguments:
   - `model` - The entity model which contains the state value, the state value setters and the transition triggers execution methods.
   - `states` - Its a dictionary of states that the state machine will use to operate
   - `transitions` - Contains the list of transitions definitions
   - `currentStateValue` - Corresponds to the initial state or current state values to be passed to the state machine

After defining the `states` and the `transitions` the state machine can be used by:
   1. Instantiating a state machine object;
   2. Triggering a state machine transition, so the machine knows to which state it will jump next. In this step it is also possible to pass arguments to be used by the transition trigger methods. These arguments are optional;
   3. And finally by executing the state machine itself, which will execute the transition trigger methods.

Code example:
```python
fsm = FSM(model, STATES, TRANSITIONS, stateValue)
fsm.triggerTransition(transitionName, data1, data2, ...)
fsm.execute()
```

## Examples
Check the following link: [examples](./examples/README.md)