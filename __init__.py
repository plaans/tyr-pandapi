from tyr.planners.model.apptainer_planner import ApptainerPlanner


# pylint: disable=too-many-ancestors
class PandaPiPlanner(ApptainerPlanner):
    """The PandaPi planner wrapped into local apptainer planner."""

    def _file_extension(self) -> str:
        return "hddl"

    def _get_apptainer_file_name(self) -> str:
        return "ppro-po-sat-gas-ff.sif"


__all__ = ["PandaPiPlanner"]
