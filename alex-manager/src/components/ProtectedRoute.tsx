import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import ApiToken from '../utils/ApiToken';

const ProtectedRoute = ({ redirectPath = '/login' }) => {
  if (!ApiToken.isLogged()) {
    return <Navigate to={redirectPath} replace />;
  }

  return <Outlet />;
};

export default ProtectedRoute;
