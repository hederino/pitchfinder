from math import log2, pow, sqrt

note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
A0 = 27.5
pitches = [f"{n}{i}" for i in range(1, 8) for n in note_names]
o2 = [f"{n}{0}" for n in note_names[-3:]]
pitches = [*o2, *pitches, "C8"]
frequencies = [A0 * pow(2, i / 12) for i, _ in enumerate(pitches)]
d = dict(zip(frequencies, pitches))


def find_closest_two(sorted_list_of_numbers, number):
    if number > sorted_list_of_numbers[-1] or number < sorted_list_of_numbers[0]:
        print("Out of range!")
        return None
    list_of_numbers = [*sorted_list_of_numbers]
    length = len(list_of_numbers)

    while length > 2:
        lower_half, upper_half = list_of_numbers[length // 2 - 1], list_of_numbers[length // 2]
        if number <= lower_half:
            list_of_numbers = list_of_numbers[:length // 2]
        elif number >= upper_half:
            list_of_numbers = list_of_numbers[length // 2:]
        else:
            return [lower_half, upper_half]
        length = len(list_of_numbers)
    return list_of_numbers


def find_closest_one(pair_of_numbers, number):
    lo, hi = pair_of_numbers
    result = hi if number >= sqrt(lo * hi) else lo
    return result


def find_closest_note(freq):
    closest_two = find_closest_two(frequencies, freq)
    if not closest_two:
        raise ValueError
    f0 = find_closest_one(closest_two, freq)
    cents = round(1200 * log2(freq / f0), 2)
    print(f"Closest pitch to {freq} Hz: {d[f0]} ({round(f0, 3)} Hz), {cents} cents difference.\n")


if __name__ == "__main__":

    while True:
        print("Enter frequency in Hz: ", end="")
        try:
            f = float(input())
            find_closest_note(f)
        except ValueError:
            print("Value error. Terminating...")
            break
