import Loan from './loan';

interface User { 
    id: number;
    username: string;
    email: string;
    first_name: string;
    last_name: string;
    loans: Loan[];
}

export default User;