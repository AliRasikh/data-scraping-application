import "tailwindcss";
import { useState } from "react";
import { ButtonContainer } from "../stylers/Button.Styler.tsx";
import { StyledButton } from "../stylers/Button.Styler.tsx";
import { ButtonSubtitle } from "../stylers/Button.Styler.tsx";
import { Title } from "../stylers/Button.Styler.tsx";

//useState: Data that changes with time, Data that can be diffrent from one point in time to another
const ButtonGroup = () => {

    const [activeButton, setActiveButton] = useState<string | null > (null);


    const handleButtonClick =(button: string) => {
        setActiveButton(button);
    };

    return (
        <>
        <Title>Select Scraping options:</Title>
        <ButtonContainer>
            <StyledButton 
                isActive={activeButton === "button1"} 
                onClick={() => handleButtonClick("button1")}
            >
                HTML Parser
                <p></p>
                <ButtonSubtitle>Basic HTML parsing for simple websites</ButtonSubtitle>
            </StyledButton>
        </ButtonContainer>
        <p></p>
        <ButtonContainer>
            <StyledButton 
                isActive={activeButton === "button2"} 
                onClick={() => handleButtonClick("button2")}
            >
                JavaScript Rendered
                <p></p>
                <ButtonSubtitle>For JavaScript-heavy websites</ButtonSubtitle>
            </StyledButton>
        </ButtonContainer>
        <p></p>
        <ButtonContainer>
            <StyledButton 
                isActive={activeButton === "button3"} 
                onClick={() => handleButtonClick("button3")}
            >
                API Endpoint
                <p></p>
                <ButtonSubtitle>Direct API calls if available</ButtonSubtitle>
            </StyledButton>
        </ButtonContainer>

        </>
            
    
    )
}
export default ButtonGroup