name: Feature Request
description: Suggest an idea for this project
title: "[FEATURE] "
labels: ["enhancement", "needs-triage"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        Thanks for suggesting a feature! ✨

  - type: checkboxes
    id: existing_feature
    attributes:
      label: Is there an existing feature request for this?
      description: Please search to see if a feature request already exists.
      options:
        - label: I have searched the existing feature requests
          required: true

  - type: textarea
    id: description
    attributes:
      label: Description
      description: A clear and concise description of what you want to happen.
      placeholder: It would be great if...
    validations:
      required: true

  - type: textarea
    id: use_case
    attributes:
      label: Use Case
      description: Describe the problem this feature would solve.
      placeholder: I want to... because...
    validations:
      required: true

  - type: textarea
    id: implementation
    attributes:
      label: Suggested Implementation (Optional)
      description: How would you implement this feature?
      placeholder: One approach could be...

  - type: textarea
    id: alternatives
    attributes:
      label: Alternatives Considered
      description: Alternative solutions or features you've considered.
      placeholder: Another approach could be...

  - type: textarea
    id: additional_context
    attributes:
      label: Additional Context
      description: Add any other context or screenshots here.
