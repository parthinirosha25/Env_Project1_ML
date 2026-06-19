def process_roster(roster):
    # Step 1: convert tuples to lists, append "active", convert back to tuples
    update_Roster = []

    #convert tuples to lists
    for driver in roster:
        driver_list = list(driver)
        print("List type ", driver_list)

        #append "active"
        driver_list.append("active")
        print("Print list:  ", driver_list)

        #convert back to tuple
        # Step 2: extract driver names into a new list
        update_Roster.append(tuple(driver_list))
        print("Upadted List value: ", update_Roster)

    # Step 3: sort names in place
    names = [driver[0] for driver in update_Roster]
    names.sort()
    print("Sorted name: ", names)

    # Step 4: count high performers (deliveries > 50)
    high_perform = 0
    for driver in roster:
        if driver[1] >50:
            high_perform += 1
    
    print("the hight performers count is: ", high_perform)

    # Step 5: return summary dictionary
    return {
        "convert tuples to lists, append \"active\", convert back to tuples: ": update_Roster,
        "Sorted Name: ": names,
        "Hight Performance count: ": high_perform
    }

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
