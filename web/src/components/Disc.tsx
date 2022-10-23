import CircleIcon from "@mui/icons-material/Circle";

interface DiscProps {
    player: string,
}

const Disc = (props: DiscProps) => {
    const {player} = props;

    const color = player;

    return (
        <CircleIcon sx={{ fontSize: 90, color: {color} }}/>
    )
}

export default Disc;