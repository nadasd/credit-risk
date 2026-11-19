"""Credit risk scoring based on the debt-to-income ratio."""

INVALID_INPUT = -1
HIGH_RISK_RATIO = 0.6
MEDIUM_RISK_RATIO = 0.3


def calculate_risk(income, debt, age):
    """Return "HIGH", "MEDIUM" or "LOW" from the debt-to-income ratio.

    Return INVALID_INPUT (-1) if income <= 0, debt < 0 or age < 0.
    """
    if income <= 0 or debt < 0 or age < 0:
        return INVALID_INPUT

    ratio = debt / income

    if ratio > HIGH_RISK_RATIO:
        return "HIGH"
    if ratio > MEDIUM_RISK_RATIO:
        return "MEDIUM"
    return "LOW"
