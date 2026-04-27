# Security Policy

## Reporting a Vulnerability

If you discover a security issue in any of the skills in this repository, please open an issue or contact the maintainer directly.

Do not publicly disclose security vulnerabilities until they are addressed.

## Scope

This repository contains AI skill definitions (SKILL.md files) and supporting scripts. It does not contain production credentials, live services, or deployable binaries.

Security reviews should focus on:
- Skill instructions that could lead to unintended data exposure or credential handling
- Scripts that read local configuration files or execute system commands
- Example inputs that may contain real user data
