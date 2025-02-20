import "tailwindcss";
import { useState } from "react";
import { ScrapeButtonContainer } from "../stylers/Scrape.Styler.tsx";
//import { StyledScrapeButton } from "../stylers/Scrape.Styler";

const ScrapeButton = () => {

    const [scrapeButton, setScrapeButton] = useState<string | null > (null);


    const handleButtonClick =(scrapebutton: string) => {
        setScrapeButton(scrapebutton);
    };

    return (
        <>
        <ScrapeButtonContainer onClick={() => handleButtonClick("scrape")}>
            Scrape Website</ScrapeButtonContainer>
        </>
    )
}
export default ScrapeButton