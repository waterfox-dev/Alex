import Book from './book';

interface Loan {
    id: number;
    book: Book;
    render_date: string;
}

export default Loan;