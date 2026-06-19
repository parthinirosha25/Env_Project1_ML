def process_roster(roster):
    # Step 1: convert tuples to lists, append "active", convert back to tuples
    update_Roster = []

    #convert tuples to lists
    for driver in roster:
        driver_list = list(driver)
        print("List type ", type(driver_list))

    #append "active"
    driver_list.append("active")
    print("Print list:  ", driver_list)

    # Step 2: extract driver names into a new list
    # Step 3: sort names in place
    # Step 4: count high performers (deliveries > 50)
    # Step 5: return summary dictionary
    pass

if __name__ == "__main__":
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
