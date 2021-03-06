#!/usr/bin/env python3

"""w01florem
Copyright (C) 2020-2021 w01f - https://github.com/w01fdev/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

########################################################################

w01f hacks from Linux for Linux!

fck capitalism, fck patriarchy, fck racism, fck animal oppression...

########################################################################
"""


import os
import random


# constants
WORDS = [
    'a', 'ab', 'accusamus', 'accusantium', 'ad', 'adipisci', 'alias',
    'aliquam', 'aliquid', 'amet', 'animi', 'aperiam', 'architecto',
    'asperiores', 'aspernatur', 'assumenda', 'at', 'atque', 'aut',
    'autem', 'beatae', 'blanditiis', 'commodi', 'consectetur',
    'consequatur', 'consequuntur', 'corporis', 'corrupti', 'culpa',
    'cum', 'cumque', 'cupiditate', 'debitis', 'delectus', 'deleniti',
    'deserunt', 'dicta', 'dignissimos', 'distinctio', 'dolor',
    'dolore', 'dolorem', 'doloremque', 'dolores', 'doloribus',
    'dolorum', 'ducimus', 'ea', 'eaque', 'earum', 'eius', 'eligendi',
    'enim', 'eos', 'error', 'esse', 'est', 'et', 'eum', 'eveniet',
    'ex', 'excepturi', 'exercitationem', 'expedita', 'explicabo',
    'facere', 'facilis', 'fuga', 'fugiat', 'fugit', 'harum', 'hic',
    'id', 'illo', 'illum', 'impedit', 'in', 'incidunt', 'inventore',
    'ipsa', 'ipsam', 'ipsum', 'iste', 'itaque', 'iure', 'iusto',
    'labore', 'laboriosam', 'laborum', 'laudantium', 'libero',
    'magnam', 'magni', 'maiores', 'maxime', 'minima', 'minus',
    'modi', 'molestiae', 'molestias', 'mollitia', 'nam', 'natus',
    'necessitatibus', 'nemo', 'neque', 'nesciunt', 'nihil', 'nisi',
    'nobis', 'non', 'nostrum', 'nulla', 'numquam', 'occaecati',
    'odio', 'odit', 'officia', 'officiis', 'omnis', 'optio',
    'pariatur', 'perferendis', 'perspiciatis', 'placeat', 'porro',
    'possimus', 'praesentium', 'provident', 'quae', 'quaerat', 'quam',
    'quas', 'quasi', 'qui', 'quia', 'quibusdam', 'quidem', 'quis',
    'quisquam', 'quo', 'quod', 'quos', 'ratione', 'recusandae',
    'reiciendis', 'rem', 'repellat', 'repellendus', 'reprehenderit',
    'repudiandae', 'rerum', 'saepe', 'sapiente', 'sed', 'sequi',
    'similique', 'sint', 'sit', 'soluta', 'sunt', 'suscipit',
    'tempora', 'tempore', 'temporibus', 'tenetur', 'totam', 'ullam',
    'unde', 'ut', 'vel', 'velit', 'veniam', 'veritatis', 'vero',
    'vitae', 'voluptas', 'voluptate', 'voluptatem', 'voluptates',
    'voluptatibus', 'voluptatum'
]


class Lorem:
    """Create a lorem ipsum text with different number of paragraphs."""

    def __init__(self, paragraphs=2, words_min=30, words_max=100):
        """Initalisation of the class.

        :param paragraphs: <int> -> default: <2>
        :param words_min: <int> -> default: <30>
        :param words_max: <int> -> default: <100>
        """

        self._paragraphs = _check_int(paragraphs)
        self._words_min = _check_int(words_min)
        self._words_max = _check_int(words_max)

    def get_paragraphs(self):
        """Returns the number of paragraphs to be created.

        :return: <int>
        """

        return self._paragraphs

    def get_words_min(self):
        """Returns the minimum number of words for the paragraph.

        :return: <int>
        """

        return self._words_min

    def get_words_max(self):
        """Returns the maximum number of words for the paragraph.

        :return: <int>
        """

        return self._words_min

    def run(self):
        """Runs the program an create a lorem ipsum text [abstract].

        :return: <list>
            returns a nested list. each list contains a sentence.
        """

        words = self._create_words()
        sentences = self._create_sentences(words)

        return sentences

    def set_paragraphs(self, paragraphs):
        """Sets the number of paragraphs to be created."""

        self._paragraphs = _check_int(paragraphs)

    def set_words_min(self, words):
        """Sets the minimum number of words for the paragraph."""

        self._words_min = _check_int(words)

    def set_words_max(self, words):
        """Sets the maximum number of words for the paragraph."""

        self._words_max = _check_int(words)

    def _create_sentences(self, paragraphs):
        """Private method for the creation of sentences.

        the paragraphs are formatted here. this means that the first
        letter of the paragraph is capitalised, there is a full stop at
        the end of the paragraph and of course a visible distance to
        another paragraph.

        :param paragraphs: <list>
            here the nested list is passed with words.
        :return: <list>
            returns a nested list. each list contains the words of the
            corresponding paragraph.
        """

        sentences = []

        for paragraph in paragraphs:
            sentence = []
            for ix, word in enumerate(paragraph):
                if ix == 0:
                    sentence.append('{} '.format(word.title()))
                if ix is not len(paragraph) - 1:
                    sentence.append('{} '.format(word))
                else:
                    sentence.append('{}.\n\n'.format(word))
            sentences.append(sentence)

        return sentences

    def _create_words(self):
        """Private method for the creation of words.

        here the words for the paragraphs are generated without
        formatting. this is done in method <_create_sentences>

        :return: <list>
            returns a nested list. each list contains the words of the
            corresponding paragraph.
        """

        words = []

        for ix in range(self._paragraphs):
            words.append(random.choices(WORDS, k=random.randint(self._words_min, self._words_max)))

        return words


class LoremFiles(Lorem):
    """Creates lorem ipsum texts and saves them in different files."""

    def __init__(self, path, files=10, folders=3, hidden=True):
        """Initalisation of the class.

        :param path: <str>
        :param files: <int>
        :param folders: <int>
        :param hidden: <bool> -> default: <True>
        """
        super().__init__()

        self._files = _check_int(files)
        self._folders = _check_int(folders)
        self._hidden = hidden
        self._path = _check_path(path)

    def get_files(self):
        """Returns the number of files to be created.

        :return: <int>
        """

        return self._files

    def get_folders(self):
        """Returns the number of folders to be created.

        :return: <int>
        """

        return self._folders

    def get_hidden(self):
        """Gets the boolean value whether hidden files are created.

        :return: <bool>
        """

        return self._hidden

    def get_path(self):
        """Return the root directory where the files are created."""

        return self._path

    def run(self):
        """Runs the program and creates the desired data structure."""

        words = self._create_words()
        sentences = self._create_sentences(words)
        self._create_files(sentences)

    def set_files(self, files):
        """Sets the number of files to be created."""

        self._files = _check_int(files)

    def set_folders(self, folders):
        """Sets the number of folders to be created."""

        self._folders = _check_int(folders)

    def set_hidden(self, hidden):
        """sets the boolean value whether hidden files are created."""

        self._hidden = hidden

    def set_path(self, path):
        """Sets the root directory where the files are created"""

        self._path = _check_path(path)

    def _create_files(self, paragraphs):
        """Creates the desired data structure."""

        with open(os.path.join(self._path, 'test.txt'), 'w') as f:
            for paragraph in paragraphs:
                [f.write('{}'.format(x)) for x in paragraph]

def _check_path(path):
    """Checks whether the directory can be created or used."""

    if isinstance(path, str):
        if os.path.exists(path):
            if not os.path.isdir(path):
                raise NotADirectoryError('<root> must be a directory')
            if not os.access(path, os.W_OK):
                raise PermissionError('no write access')
        else:
            raise NotADirectoryError('directory does not exist')
    else:
        raise TypeError('argument must be type <str>')

    return path


def _check_int(value):
    """Checks whether <int> value is passed -> else exception error.

    :param value: <int>
    :return: <int>
    """

    if not isinstance(value, int):
        raise TypeError('only <int> allowed')

    return value


def main():
    """Main function of the program."""


if __name__ == '__main__':
    main()
