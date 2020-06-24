export const getNeighborhoodsList = () => {
  sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  addNeighborhood = (newNeighborhood) => {
    sanFranciscoNeighborhoods.push(newNeighborhood);
    return sanFranciscoNeighborhoods;
  };
};
