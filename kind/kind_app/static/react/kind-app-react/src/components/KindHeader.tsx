import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';


const Header: React.FC = () => {
    return (
        <Box sx={{ width: '100%', maxWidth: 600 }}>
            <Typography variant="h2" gutterBottom>
                Welcome to Kind.
            </Typography>
        </Box>
    );
}

export default Header;