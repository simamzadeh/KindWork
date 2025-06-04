import React, { useEffect, useState } from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import { useApi } from '../hooks/useApi';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';

export interface KudosEntryCardProps {}

const KudosEntryCard: React.FC<KudosEntryCardProps> = () => {
  const [data, setData] = useState<any[]>([]); // add props in useState
  const {fetchWithTokens} = useApi();

  useEffect(() => {
      fetchWithTokens("api/kudos/", { 
        method: 'GET', 
        })
        .then((response: any) => {
          console.log(data);
          setData(data);
        })
        .catch((error: any) =>
          console.log("Failed to list data")
        );
  }, [fetchWithTokens]);

return (
  <React.Fragment>
    <CardContent>
      <Typography gutterBottom sx={{ color: 'text.secondary', fontSize: 14 }}>
        Give Kudos
      </Typography>
      <Typography variant="h5" component="div">
        Who do you have to appreciate?
      </Typography>
      <TextField
            id="outlined-basic"
            placeholder="I give kudos to..."
            multiline
            minRows={5}
            maxRows={5}
            sx={{ width: '100%', backgroundColor: '#fff' }}
      />
      <List>
          {data.length > 0 ? (
            data.map((entry, index) => (
              <ListItem key={index}>
                <ListItemText
                  primary={entry.title || `Entry #${index + 1}`} // Assuming each entry has a 'title' field
                  secondary={entry.description || 'No description available'} // Assuming each entry has a 'description' field
                />
              </ListItem>
            ))
          ) : (
            <Typography variant="body2" sx={{ color: 'text.secondary', marginTop: 2 }}>
              No kudos entries found.
            </Typography>
          )}
        </List>
    </CardContent>
  </React.Fragment>
);

}

export default function OutlinedCard() {
  return (
    <Box sx={{ 
      minWidth: 275, 
    }}>
      <Card variant="outlined">{<KudosEntryCard/>}</Card>
    </Box>
  );
}