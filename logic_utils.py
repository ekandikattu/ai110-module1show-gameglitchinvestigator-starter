# FIX: Refactored logic into logic_utils.py using Copilot Agent mode

DIFFICULTY_RANGES = {
    "Easy": (1, 20),
    "Normal": (1, 100),
    "Hard": (1, 50),
}

DIFFICULTY_ATTEMPT_LIMITS = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    return DIFFICULTY_RANGES.get(difficulty, DIFFICULTY_RANGES["Normal"])


def get_attempt_limit_for_difficulty(difficulty: str):
    """Return the attempt limit for a given difficulty."""
    return DIFFICULTY_ATTEMPT_LIMITS.get(
        difficulty,
        DIFFICULTY_ATTEMPT_LIMITS["Normal"],
    )

# FIX: Ensure that reset_game_state uses the selected difficulty settings to generate the new secret number, and that the test verifies this behavior.
def reset_game_state(session_state, difficulty: str, randint_func):
    """Reset the game state using the selected difficulty settings."""
    low, high = get_range_for_difficulty(difficulty)
    session_state["secret"] = randint_func(low, high)
    session_state["attempts"] = 0
    session_state["score"] = 0
    session_state["status"] = "playing"
    session_state["history"] = []
    session_state["active_difficulty"] = difficulty


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
