import React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import { styled } from "@mui/material/styles";
import { Info, InfoTitle } from "../mui-treasury/info-basic";

const StyledCard = styled(Card)(() => ({
  position: "relative",
  borderRadius: 16,
  padding: 12,
  backgroundColor: "#e5fce6",
  minWidth: 300,
  boxShadow: "0 0 20px 0 rgba(0,0,0,0.12)",
  transition: "0.3s",
  "&:hover": {
    transform: "translateY(-3px)",
    boxShadow: "0 4px 20px 0 rgba(0,0,0,0.12)",
  },
}));

const LogButton = styled(Button)(() => ({
  backgroundColor: "#fff !important",
  color: "#193b1e",
  boxShadow: "0 2px 6px #d0efef",
  borderRadius: 12,
  minWidth: 120,
  minHeight: 4,
  textTransform: "initial",
  fontSize: "0.875rem",
  fontWeight: 700,
  letterSpacing: 0,
}));

const StyledDiv = styled("div")(() => ({
  position: "absolute",
  bottom: 0,
  right: 0,
  transform: "translate(70%, 50%)",
  borderRadius: "50%",
  backgroundColor: "rgba(71, 167, 162, 0.12)",
  padding: "40%",

  "&:before": {
    position: "absolute",
    borderRadius: "50%",
    content: '""',
    display: "block",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    margin: "-16%",
    backgroundColor: "rgba(71, 167, 162, 0.08)",
  },
}));

const InfoStyles = () => {
  return {
    title: {
      color: "#193b1e",
      fontSize: "1.5rem",
      fontWeight: 700,
      lineHeight: 1.6,
      letterSpacing: "0.0075em",
      marginBottom: 0,
    },
    subtitle: {
      color: "#193b1e",
      fontSize: "0.875rem",
      fontWeight: 500,
    },
  };
};

export function QuestionButtonCard() {
  return (
    <StyledCard>
      <Box sx={{ display: "flex", flexDirection: "column", gap: 2, mr: 2 }}>
        <Info useStyles={InfoStyles}>
          <InfoTitle>What are you grateful for?</InfoTitle>
        </Info>
        <Box sx={{ mt: 2 }}>
          <LogButton>Log entry</LogButton>
        </Box>
      </Box>
      <StyledDiv />
    </StyledCard>
  );
}

export default QuestionButtonCard;