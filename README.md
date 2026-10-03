# Multi-Agent Debate System

A real-time multi-agent AI debate framework for orchestrating structured conversations between autonomous language agents. The project is designed to simulate intellectual debate, role-based reasoning, and collaborative or adversarial decision making in a controlled environment.

This repository combines:
- Python for backend orchestration and agent logic
- HTML, CSS, and JavaScript for the user-facing interface
- LLM-powered agents for reasoning, rebuttal, and synthesis

## Overview

The system allows multiple AI agents to participate in a shared debate around a topic or problem. Each agent can be assigned a role, perspective, or strategy, and the platform coordinates their responses in a structured sequence.

Common use cases include:
- multi-agent reasoning
- debate simulation
- collaborative decision support
- adversarial evaluation of ideas
- research on agent communication and consensus-building

## Core Concepts

The application is built around a few essential ideas:

- Agent roles: each participant has a specialized perspective or behavior
- Debate loop: agents respond in sequence or rounds
- Orchestration layer: manages turn flow, timing, and conversation state
- Context memory: tracks previous arguments and discussion progression
- Final synthesis: combines arguments into a conclusion or summary

## Features

- Multi-agent debate orchestration
- Role-based agent behavior
- Structured conversation flow
- Real-time argument exchange
- Rebuttal and synthesis supported by the debate engine
- Extensible agent architecture
- Browser-based interface for user interaction
- Configurable model and prompt behavior

## Architecture

The project is organized around a simple architecture:

- Frontend: web interface for starting debates and viewing outputs
- Backend: Python services that manage agent coordination
- Debate engine: controls rounds, context, roles, and final evaluation
- LLM integration: sends prompts to the model(s) used by agents
- State management: tracks conversation flow and generation history
