import { Dispatch, SetStateAction } from "react";


type RadioOption = "scrape1" | "scrape2" | "scrape3";

type RadioButtonsProps = {
  setter: Dispatch<SetStateAction<RadioOption>>;
  getter: string;
};

const RadioButtonsExample: React.FC<RadioButtonsProps> = ({ setter, getter }) => {

  const handleOptionChange = (event: React.ChangeEvent<HTMLInputElement>) => {
   setter(event.target.value as RadioOption);
  };

  return (
    <div style={{background:"gray",padding:"10px",borderRadius:"10px"}}>
      <h3>Selectează o opțiune:</h3>
      <label>
        <input
          type="radio"
          name="options"
          value="scrape1"
          checked={getter === "scrape1"}
          onChange={handleOptionChange}
        />
        hallo
      </label>
      <br />

      <label>
        <input
          type="radio"
          name="options"
          value="scrape2"
          checked={getter === "scrape2"}
          onChange={handleOptionChange}
        />
        B
      </label>
      <br />

      <label>
        <input
          type="radio"
          name="options"
          value="scrape3"
          checked={getter === "scrape3"}
          onChange={handleOptionChange}
        />
        C
      </label>
      
      <p>Opțiunea selectată este: {getter.toUpperCase()}</p>
    </div>
  );
};

export default RadioButtonsExample;
