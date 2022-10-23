import CircleIcon from "@mui/icons-material/Circle";

interface DiscProps {
    player: string,
}

const Disc = (props: DiscProps) => {
    const {player} = props;

    const color = player;

    return (
        <CircleIcon sx={{ fontSize: 75, color: {color}, padding: 0, margin: 0 }}/>
    )
}

export default Disc;