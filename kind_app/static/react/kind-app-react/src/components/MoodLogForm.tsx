import React, { useState } from 'react';
import { Box, Typography, Slider, Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

interface MoodLogFormProps {
    open: boolean;
    onClose: () => void;
    onSubmit: (mood: string) => void;  // Ensure the mood string is passed correctly
}

// Define the mood labels
const moodMarks = [
  { value: 0, label: 'Very Unpleasant' },
  { value: 30, label: 'Unpleasant' },
  { value: 50, label: 'Neutral' },
  { value: 70, label: 'Pleasant' },
  { value: 100, label: 'Very Pleasant' },
];

// Create a map to convert label to backend-accepted lowercase values
const moodMap: { [key in typeof moodMarks[number]['label']]: string } = {
  'Very Unpleasant': 'very unpleasant',
  'Unpleasant': 'unpleasant',
  'Neutral': 'neutral',
  'Pleasant': 'pleasant',
  'Very Pleasant': 'very pleasant',
};

const MoodLogForm: React.FC<MoodLogFormProps> = ({ open, onClose, onSubmit }) => {
  const [mood, setMood] = useState<number>(50);  // Default to Neutral (50)

  // Handle the change of the mood slider
  const handleMoodChange = (_: Event, newValue: number | number[]) => {
    setMood(newValue as number);  // Treat newValue as a number
  };

  // Handle the form submission
  const handleSubmit = () => {
    const selectedMoodLabel = moodMarks.find((mark) => mark.value === mood)?.label || 'Neutral';  // Find the label
    const selectedMood = moodMap[selectedMoodLabel];  // Map the label to the backend format
    onSubmit(selectedMood);  // Submit the selected mood in the backend-accepted format
    console.log("Submitted mood:", selectedMood);  // Log the submitted mood
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="md" fullWidth>
      <DialogTitle>Log Your Mood</DialogTitle>
      <DialogContent sx={{ width: '100%', maxWidth: '600px', mx: 'auto', paddingLeft: '24px', paddingRight: '24px'}}>
        <Box sx={{ width: '100%', padding: '24px'}}>
          <Typography gutterBottom >Your Current Mood</Typography>

          <Slider
            value={mood}
            onChange={handleMoodChange}
            step={25}
            marks={moodMarks}
            min={0}
            max={100}
            sx={{
                marginTop: '40px',
                marginBottom: '40px',
                height: '8px',
                '& .MuiSlider-thumb': {
                  width: '24px',
                  height: '24px',
                },
                '& .MuiSlider-markLabel': {
                  fontSize: '1rem',  // Adjust font size if needed
                  whiteSpace: 'nowrap',  // Prevent text from wrapping
                  overflow: 'visible',  // Ensure text is not cut off
                },
                '& .MuiSlider-mark': {
                  transform: 'translateX(-50%)',  // Adjust positioning of the marks
                },
                '& .MuiSlider-markLabel[data-index="0"]': {  // First label (Very Unpleasant)
                  transform: 'translateX(0%)',  // Ensure it's fully visible
                  marginLeft: '-12px',  // Add some left margin to make space
                },
                '& .MuiSlider-markLabel[data-index="4"]': {  // Last label (Very Pleasant)
                  transform: 'translateX(-100%)',  // Ensure it's fully visible
                  marginRight: '-12px',  // Add some right margin to make space
                },
              }}
          />
        </Box>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} color="secondary">
          Cancel
        </Button>
        <Button onClick={handleSubmit} color="primary">
          Submit
        </Button>
      </DialogActions>
    </Dialog>
  );
};

export default MoodLogForm;
