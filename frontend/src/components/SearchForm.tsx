import { useState } from "react";

type SearchFormProps = {
  onSearch: (ciudad: string) => Promise<void>;
};

const SearchForm = ({ onSearch }: SearchFormProps) => {
  const [city, setCity] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!city.trim()) return;

    await onSearch(city);
    setCity("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Ingresa una ciudad"
        value={city}
        onChange={(e) => setCity(e.target.value)}
      />
      <button type="submit">Buscar</button>
    </form>
  );
};

export default SearchForm;
