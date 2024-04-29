import React, { useState, useEffect } from "react";
import { Chip, Sheet } from "@mui/joy";
import Table from "@mui/joy/Table";

import Author from "../types/author";
import Availability from "../types/availability";
import Shelf from "../types/shelf";
import State from "../types/state";
import Publisher from "../types/publisher";

interface Book {
  id: number;
  isbn: string;
  title: string;
  authors: Author[];
  shelf: Shelf;
  state: State;
  cover: string;
  publisher: Publisher;
  availability: Availability;
}

function BookList(){

  const [data, setData] = useState<Book[]>([]);

  useEffect(() => {
    onLoad();
  }, []);

  function onLoad(){
    fetch('http://localhost:8000/api/books')
      .then(response => response.json())
      .then((books: Book[]) => {
        setData(books);
      })
      .catch(error => console.error('Error fetching books:', error));
  }

  return (
    <Sheet>
      <Table>
        <thead>
          <tr>
            <th>ID</th>
            <th>ISBN</th>
            <th>Title</th>
            <th>Shelf</th>
            <th>State</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {data.map((book) => (
            <tr key={book.id}>
              <td>{book.id}</td>
              <td>{book.isbn}</td>
              <td>{book.title}</td>
              <td>{book.shelf.name}</td>
              <td>{book.state.name}</td>
              <td>
                {book.availability.id == 1 ? 
                  <Chip color="success">{book.availability.name}</Chip> : <Chip color="danger">{book.availability.name}</Chip>
                }
              </td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Sheet>
  );
}

export default BookList;
