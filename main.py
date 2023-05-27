from note import Note, note_a4
from message import Message

A4 = 440.0
A4_MAX, A4_MIN = 500.0, 400.0


def set_a4(freq_a4):

    while True:
        f = input(Message.prompt_a4(note_a4, freq_a4)).strip().lower()
        if f == "x":
            print(Message.back_to_main)
            break
        try:
            new_a4 = float(f)
            if A4_MIN <= new_a4 <= A4_MAX:
                return new_a4
            print(Message.a4_out_of_range(note_a4, A4_MIN, A4_MAX))
        except ValueError:
            print(Message.invalid_freq)

def main(freq_a4=A4):

    print(Message.welcome)
    print(Message.info(note_a4, freq_a4))

    while True:
        
        i = input(Message.enter_freq).strip().lower()
        
        if i == "x":
            print(Message.bye)
            break
        
        if i == "f":
            new_a4 = set_a4(freq_a4)
            if new_a4:
                print(Message.a4_set(note_a4, freq_a4, new_a4))
                freq_a4 = new_a4                

        else:
            try:
                freq = float(i)
                note, cents_diff = Note.freq_to_note(freq, freq_a4)
                note_str = str(note) if note.is_natural else f"{note}/{note.enharmonic_note()}"
                note_0_cents_freq = note.note_to_freq(freq_a4)
                print(Message.closest(freq, note_str, note_0_cents_freq, cents_diff))
            except ValueError:
                print(Message.invalid_freq)


if __name__ == "__main__":
    main()
