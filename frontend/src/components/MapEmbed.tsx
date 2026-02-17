interface Props {
  lat: number;
  lng: number;
}

const MapEmbed = ({ lat, lng }: Props) => {
  const API_KEY = import.meta.env.VITE_GOOGLE_API_KEY; 

  const src = `https://www.google.com/maps/embed/v1/view?key=${API_KEY}&center=${lat},${lng}&zoom=14`;

  return (
    <iframe
      width="100%"
      height="300"
      style={{ border: 0, marginTop: '20px', borderRadius: '12px' }}
      src={src}
      allowFullScreen
      loading="lazy"
    />
  );
};

export default MapEmbed;