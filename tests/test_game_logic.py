from logic_utils import check_guess, get_attempt_limit_for_difficulty, reset_game_state


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_check_guess_hint_direction_regression():
    # Regression test for the historical bug where hint directions were inverted.
    too_high_outcome, too_high_message = check_guess(75, 50)
    too_low_outcome, too_low_message = check_guess(25, 50)

    assert too_high_outcome == "Too High"
    assert too_high_message == "📉 Go LOWER!"
    assert too_low_outcome == "Too Low"
    assert too_low_message == "📈 Go HIGHER!"


def test_reset_game_state_uses_selected_difficulty_settings():
    calls = []

    def fake_randint(low, high):
        calls.append((low, high))
        return high

    session_state = {
        "secret": 42,
        "attempts": 7,
        "score": 25,
        "status": "lost",
        "history": [10, 20, 30],
        "active_difficulty": "Normal",
    }

    reset_game_state(session_state, "Easy", fake_randint)

    assert calls == [(1, 20)]
    assert session_state["secret"] == 20
    assert session_state["attempts"] == 0
    assert session_state["score"] == 0
    assert session_state["status"] == "playing"
    assert session_state["history"] == []
    assert session_state["active_difficulty"] == "Easy"
    assert get_attempt_limit_for_difficulty("Easy") == 6
