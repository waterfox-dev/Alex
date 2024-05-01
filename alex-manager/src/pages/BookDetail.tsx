import React, { useState, useEffect } from "react";

import { useParams } from "react-router-dom";

import { Chip, Sheet } from "@mui/joy";

import Book from "../types/book";


function BookDetail(){
    const { id } = useParams();
    
    const [book, setBook] = useState<Book | null>(null);
    
    useEffect(() => {
        onLoad();
    }, []);
    
    function onLoad(){
        console.log(id)
        fetch(`http://localhost:8000/api/books/${id}`)
        .then(response => response.json())
        .then((book: Book) => {
            setBook(book);
        })
        .catch(error => console.error('Error fetching book:', error));
    }
    
    return (
        <div>
        <h1>Book</h1>
        {book && (
            <Sheet>
            <h2>{book.title}</h2>
            <p>ISBN: {book.isbn}</p>
            <p>Shelf: {book.shelf.name}</p>
            <p>State: {book.state.name}</p>
            <p>Publisher: {book.publisher.name}</p>
            <p>Authors: {book.authors.map((author) => author.name + " "  + author.first_name).join(', ')}</p>
            <p>
                Status: {book.availability.id === 1 ? 
                <Chip color="success">{book.availability.name}</Chip> : <Chip color="danger">{book.availability.name}</Chip>
                }
            </p>
            <img src={book.cover} alt={book.title} style={{maxWidth: '100%'}}/>
            </Sheet>
        )}
        </div>
    );
}

export default BookDetail;