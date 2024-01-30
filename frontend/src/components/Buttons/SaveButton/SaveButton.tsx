import "./SaveButton.css"
import { toast } from "react-toastify";


interface SaveButtonProps {
  selectedCurrencies: string[];
  disabled: boolean
}

export const SaveButton: React.FC<SaveButtonProps> = ({ selectedCurrencies, disabled }) => {
  return (
    <div>
      <button>Save to server</button>    
    </div>
  );
};

export default SaveButton;