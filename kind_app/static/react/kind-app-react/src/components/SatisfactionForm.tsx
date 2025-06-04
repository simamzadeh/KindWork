import React, { useState } from 'react';
import { Box, Typography, Slider, Button, Dialog, DialogActions, DialogContent, DialogTitle } from '@mui/material';

interface SatisfactionFormProps {
    open: boolean;
    onClose: () => void;
    onSubmit: (satisfaction: string) => void;  // Ensure the satisfaction string is passed correctly
}

// Define the satisfaction labels
const satisfactionMarks = [
  { value: 0, label: 'Very Unhappy' },
  { value: 25, label: 'Unhappy' },
  { value: 50, label: 'Neutral' },
  { value: 75, label: 'Content' },
  { value: 100, label: 'Very Content' },
];

// Create a map to convert label to backend-accepted lowercase values
const satisfactionMap: { [key in typeof satisfactionMarks[number]['label']]: string } = {
  'Very Unhappy': 'very unhappy',
  'Unhappy': 'unhappy',
  'Neutral': 'neutral',
  'Content': 'content',
  'Very Content': 'very content',
};

const SatisfactionForm: React.FC<SatisfactionFormProps> = ({ open, onClose, onSubmit }) => {
  const [satisfaction, setSatisfaction] = useState<number>(50);  // Default to Neutral (50)

  // Handle the change of the satisfaction slider
  const handleSatisfactionChange = (_: Event, newValue: number | number[]) => {
    setSatisfaction(newValue as number);  // Treat newValue as a number
  };

  // Handle the form submission
  const handleSubmit = () => {
    const selectedSatisfactionLabel = satisfactionMarks.find((mark) => mark.value === satisfaction)?.label || 'Neutral';  // Find the label
    const selectedSatisfaction = satisfactionMap[selectedSatisfactionLabel];  // Map the label to the backend format
    onSubmit(selectedSatisfaction);  // Submit the selected satisfaction in the backend-accepted format
    console.log("Submitted satisfaction:", selectedSatisfaction);  // Log the submitted satisfaction
  };

  return (
    <Dialog open={open} onClose={onClose} maxWidth="md" fullWidth>
      <DialogTitle>Log Your Daily Satisfaction</DialogTitle>
      <DialogContent sx={{ width: '100%', maxWidth: '600px', mx: 'auto', paddingLeft: '24px', paddingRight: '24px'}}>
        <Box sx={{ width: '100%', padding: '24px'}}>
          <Typography gutterBottom >Your Current Satisfaction</Typography>

          <Slider
            value={satisfaction}
            onChange={handleSatisfactionChange}
            step={25}
            marks={satisfactionMarks}
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
                '& .MuiSlider-markLabel[data-index="0"]': {  // First label (Very Unhappy)
                  transform: 'translateX(0%)',  // Ensure it's fully visible
                  marginLeft: '-12px',  // Add some left margin to make space
                },
                '& .MuiSlider-markLabel[data-index="4"]': {  // Last label (Very Content)
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

export default SatisfactionForm;
