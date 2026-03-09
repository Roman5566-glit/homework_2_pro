events = []


def add_event(event):
    """Adds new event"""
    events.append(event)


def remove_event(event):
    """Removes event if it exists"""
    if event in events:
        events.remove(event)


def show_events():
    """Shows all events"""
    print("Майбутні події:", events)


add_event("Екзамен")
add_event("Тренування")

show_events()

remove_event("Екзамен")

show_events()
