import React from 'react';

import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom';

import BookList from './pages/BookList';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/books" element={<BookList/>}/>
      </Routes>
    </Router>
  );
}

export default App;
