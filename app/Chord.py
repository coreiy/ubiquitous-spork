BASE_NOTES = [key+str(octave)
              for octave in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
              for key in ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']]

CHORD_PATTERNS = {
    'minor': [0, 3, 7],
    'major': [0, 4, 7],
    'augmented': [0, 4, 8],
    'diminished': [0, 3, 6],
    'sus2': [0, 2, 7],
    'sus4': [0, 5, 7],
    'minor_7th': [0, 3, 7, 10],
    'major_7th': [0, 4, 7, 11],
    'dominant_7th': [0, 4, 7, 10],
    'minor_9th': [0, 3, 7, 10, 14],
    'major_9th': [0, 4, 7, 11, 14],
    'dominant_9th': [0, 4, 7, 10, 14],
    'minor_11th': [0, 3, 7, 10, 17],
    'major_11th': [0, 4, 7, 11, 17]
}

CHORD_PROGRESSION_PATTERNS = {
    'c_minor': [
        {'steps_up': 2, 'chord': 'minor_7th'}]}


class Note:

    def __init__(self, note: str):
        self.note = note

    def __str__(self):
        return self.note

    def index(self):
        return BASE_NOTES.index(self.note)

    def transpose(self, semitones: int):
        return Note(BASE_NOTES[self.index()+semitones])

    def chord(self, pattern):
        return Chord(self.note, pattern)


class Chord:

    def __init__(self, root_note, chord_name):
        self.root_note = Note(root_note)
        self.chord_name = chord_name
        self.notes = [Note(root_note).transpose(semitones)
                      for semitones in CHORD_PATTERNS[chord_name]]        
        self.notes.sort(key=lambda x: x.index())
        self.chord = self.get_chord_pattern()

    def __str__(self):
        chord = ' '.join([str(self.root()), self.get_chord_name()])
        in_keys = str([str(note) for note in self.notes])
        return ' '.join([chord, str(self.chord), in_keys])

    def get_chord_pattern(self):
        return [note.index()-self.notes[0].index()
                for note in self.notes]

    def root(self):
        return self.notes[0]

    def is_chord(self, chord):
        return self.chord == chord

    def get_chord_name(self):
        for key, value in CHORD_PATTERNS.items():
            if (self.is_chord(value)):
                return key
        return None

    def transpose(self, semitones: int):
        return Chord([Note(note).transpose(semitones)
                      for note in self.notes])


if __name__ == '__main__':
    lowest_octave = 3
    highest_octave = 5
    lower_notes = BASE_NOTES[0+(12*lowest_octave):12*highest_octave]

    chords = [Chord(first_note, key)
              for first_note in lower_notes
              for key, _ in CHORD_PATTERNS.items()]

    for chord in chords:
        print(chord)

    print(Note('F3').chord('minor'))
