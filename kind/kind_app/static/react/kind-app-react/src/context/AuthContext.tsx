import React, {
  createContext,
  useState,
  useContext,
  useEffect,
  ReactNode,
} from 'react';
import Cookies from 'js-cookie';
import { DOMAIN } from '../constants';

interface AuthContextType {
  csrfToken: string | null;
  setCSRFToken: React.Dispatch<React.SetStateAction<string | null>>;
}

const AuthContext = createContext<AuthContextType | null>(null);

interface AuthProviderProps {
  children: ReactNode;
}

export function AuthProvider({ children }: AuthProviderProps) {
  const [csrfToken, setCSRFToken] = useState<string | null>(
    Cookies.get('csrftoken') || null
  );

  useEffect(() => {
    if (!csrfToken) {
      fetchCSRFToken().then((token) => {
        if (token) {
          setCSRFToken(token);
          Cookies.set('csrftoken', token, { expires: 1 });
        }
      });
    }
  }, [csrfToken]);


  return (
    <AuthContext.Provider
      value={{
        csrfToken,
        setCSRFToken,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth(): AuthContextType {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within a AuthProvider Context');
  }
  return context;
}

async function fetchCSRFToken(): Promise<string | null> {
  try {
    const response = await fetch(`${DOMAIN}/api/security/get-csrf-token/`, {
      credentials: 'include',
    });
    if (response.ok) {
      const csrfToken = Cookies.get('csrftoken');
      return csrfToken || null;
    }
    throw new Error('Failed to fetch CSRF token');
  } catch (error) {
    console.error('Error fetching CSRF token:', error);
    return null;
  }
}
