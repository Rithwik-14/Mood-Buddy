def get_mood_response(mood):
    responses = {
        "😔Sad": {
            "quote": "Tough times don’t last, tough people do.",
            "action": "Take 3 deep breaths and write down one thing you're grateful for.",
            "music": "https://www.youtube.com/watch?v=5qap5aO4i9A"
        },
        "😣Stressed": {
            "quote": "You can’t calm the storm, so stop trying. Calm yourself, the storm will pass.",
            "action": "Go outside for 2 mins. Just walk.",
            "music": "https://www.youtube.com/watch?v=lTRiuFIWV54"
        },
        "😠Angry": {
            "quote": "Don’t let your emotions overpower your intelligence.",
            "action": "Drink a glass of water. Sit in silence for 1 min.",
            "music": "https://www.youtube.com/watch?v=2OEL4P1Rz04"
        },
        "😴Tired": {
            "quote": "Rest if you must, but don’t you quit.",
            "action": "Do a light stretch or close your eyes for 3 mins.",
            "music": "https://www.youtube.com/watch?v=hHW1oY26kxQ"
        },
        "😄Happy": {
            "quote": "Enjoy this moment fully. You earned it!",
            "action": "Share your joy with someone 😊",
            "music": "https://www.youtube.com/watch?v=9Qk7IyUdeOE"
        },
        "😕Lost": {
            "quote": "You might feel lost, but you're just getting recalibrated.",
            "action": "Write 3 things you want to explore in life.",
            "music": "https://www.youtube.com/watch?v=DWcJFNfaw9c"
        },
        "😰Anxious": {
            "quote": "Anxiety is a wave — let it rise, let it pass.",
            "action": "Take slow deep breaths. Try 4-7-8 breathing.",
            "music": "https://youtu.be/MIr3RsUWrdo"
        },
        "🙏Grateful": {
            "quote": "Gratitude turns what we have into enough.",
            "action": "Write down 3 things you're grateful for right now.",
            "music": "https://youtu.be/y6Sxv-sUYtM"
        },

    }
    return responses.get(mood, {})
