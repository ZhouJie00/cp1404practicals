from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input("Choose an option: ").lower()

        if user_choice == 'q':
            print(f"Total bill: ${total_bill:.2f}")
            break
        elif user_choice == 'c':
            print("Taxis available:")
            list_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
                print(f"Bill to date: ${total_bill:.2f}")
            except IndexError:
                print("Invalid taxi choice")
        elif user_choice == 'd':
            if current_taxi:
                distance = float(input("Drive how far? "))
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
                print(f"Bill to date: ${total_bill:.2f}")
                current_taxi.start_fare()
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")


def list_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


if __name__ == '__main__':
    main()