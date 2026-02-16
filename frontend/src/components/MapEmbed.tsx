interface Props {
  lat: number;
  lng: number;
}

const MapEmbed = ({ lat, lng }: Props) => {
  const src = `https://www.google.com/maps/embed/v1/view?key=TU_GOOGLE_MAPS_KEY&center=${lat},${lng}&zoom=10`;

  return (
    <iframe
      width="600"
      height="450"
      style={{ border: 0 }}
      loading="lazy"
      allowFullScreen
      src={src}
    />
  );
};

export default MapEmbed;
