def print_seat(seat):
    for item in seat:
        print("${}".format(item))
    print("-"*15)
    total = get_seat_total(seat)
    print("Total: ${}".format(total))

def get_seat_total(seat):
    total = 0
    for dish in seat:
        total = total + dish
    return total

def main():
    seats = [[19.95],
            [20.45 + 3.10],
            [7.00/2, 2.10, 21.45],
            [7.00/2, 2.10, 14.99]
            ]
    grand_total = 0
    for seat in seats:
        print_seat(seat)
        grand_total = grand_total + get_seat_total(seat)
        print("\n")
        print("="*15)
        print("Grand total: ${}".format(grand_total))

if __name__ == "__main__":
    main()
