def process_roster(roster):
    updated_roster = []

    for driver in roster:
        driver_list = list(driver)
        driver_list.append("active")
        print("Print list:  ", driver_list)
        updated_roster.append(tuple(driver_list))

    names = [driver[0] for driver in updated_roster]
    names.sort()
    print("Print name is:  ", names)

    high_performers = 0
    for driver in roster:
        if driver[1] > 50:
            high_performers += 1

    return {
        "updated_roster": updated_roster,
        "sorted_names": names,
        "high_performers": high_performers
    }


sample_roster = [
    ("Chen Wei", 63),
    ("Maria Santos", 45),
    ("Carlos Mendes", 78),
    ("Fatima Al-Amin", 50),
    ("Kofi Mensah", 91),
    ("Lena Fischer", 30),
    ("Takeshi Yamamoto", 55),
]

print(process_roster(sample_roster))