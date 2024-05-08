import Author from './author';
import Shelf from './shelf';
import State from './state';
import Publisher from './publisher';

interface Book {
  id: number;
  isbn: string;
  title: string;
  authors: Author[];
  shelf: Shelf;
  state: State;
  cover: string;
  publisher: Publisher;
  availability: string;
}

export default Book;