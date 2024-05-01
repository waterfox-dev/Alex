import React from 'react';

import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';

import BookList from './pages/BookList';
import BookDetail from './pages/BookDetail';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/books" element={<BookList/>}/>
        <Route path="/books/:id" element={<BookDetail/>}/>
      </Routes>
    </Router>
  );
}

export default App;
