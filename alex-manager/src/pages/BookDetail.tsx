import { useParams } from "react-router-dom";
import { Chip, CircularProgress, Sheet } from "@mui/joy";
import Book from "../types/book";
import { useQuery } from "@tanstack/react-query";
import BookChip from "../components/BookChip";
import ConnectionErrorModal from "../components/ConnectionErrorModal";

function BookDetail() {
    const { id } = useParams();

    const { data, isLoading, isError } = useQuery({
        queryKey: ['book'],
        queryFn: () => fetch(`http://localhost:8000/api/books/${id}`).then(res => res.json()),
    });

    if (isLoading) return <CircularProgress value={10}/>
    if (isError) return <ConnectionErrorModal />
    return (
        <div>
            <h1>{data.title}</h1>
            {data as Book && (
                <Sheet>
                    <p>ISBN: {data.isbn}</p>
                    <p>Shelf: {data.shelf.name}</p>
                    <p>State: {data.state.name}</p>
                    <p>Publisher: {data.publisher.name}</p>
                    <p>Authors: {data.authors.map((author: { name: string; first_name: string; }) => author.name + " " + author.first_name).join(', ')}</p>
                    <p>Availability: <BookChip availability={data.availability} /></p>
                    <img src={data.cover} alt={data.title} style={{ maxWidth: '100%' }} />
                </Sheet>
            )}
        </div>
    );
}

export default BookDetail;
