name: Bug Report
description: Report a bug in the application
title: "[BUG] "
labels: ["bug", "needs-triage"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to file a bug report! 🐛

  - type: checkboxes
    id: existing_issue
    attributes:
      label: Is there an existing issue for this?
      description: Please search to see if an issue already exists for the bug you encountered.
      options:
        - label: I have searched the existing issues
          required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      description: Provide a clear and concise description of what the bug is.
      placeholder: A bug is when something doesn't work as expected...
    validations:
      required: true

  - type: textarea
    id: steps_to_reproduce
    attributes:
      label: Steps to Reproduce
      description: Steps to reproduce the behavior.
      placeholder: |
        1. Go to '...'
        2. Click on '...'
        3. Scroll down to '...'
        4. See error
    validations:
      required: true

  - type: textarea
    id: expected_behavior
    attributes:
      label: Expected Behavior
      description: What should happen instead?
      placeholder: Describe what you expected to happen...
    validations:
      required: true

  - type: textarea
    id: actual_behavior
    attributes:
      label: Actual Behavior
      description: What actually happened?
      placeholder: Describe what actually happened...
    validations:
      required: true

  - type: textarea
    id: screenshots
    attributes:
      label: Screenshots
      description: If applicable, add screenshots to help explain the problem.

  - type: textarea
    id: environment
    attributes:
      label: Environment
      description: Information about your environment
      value: |
        - OS: [e.g., macOS 13.0]
        - Python Version: [e.g., 3.10]
        - Django Version: [e.g., 6.0]
        - Browser: [e.g., Chrome 120]
    validations:
      required: true

  - type: textarea
    id: additional_context
    attributes:
      label: Additional Context
      description: Add any other context about the problem here.
