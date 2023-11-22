import joblib
import pandas as pd
import datetime
from evidently.metrics import ClassificationClassBalance
from evidently.metrics import ClassificationConfusionMatrix
from evidently.metrics import ClassificationDummyMetric
from evidently.metrics import ClassificationQualityByClass
from evidently.metrics import ClassificationQualityMetric
from evidently.metrics import DatasetDriftMetric
from evidently.metrics import DatasetMissingValuesMetric
from evidently.report import Report
from evidently.ui.dashboards import CounterAgg
from evidently.ui.dashboards import DashboardPanelCounter
from evidently.ui.dashboards import DashboardPanelPlot
from evidently.ui.dashboards import PanelValue
from evidently.ui.dashboards import PlotType
from evidently.ui.dashboards import ReportFilter
from evidently.ui.workspace import Workspace
from evidently.ui.workspace import WorkspaceBase

WORKSPACE = "workspace2"

YOUR_PROJECT_NAME = "Monitoring Model"
YOUR_PROJECT_DESCRIPTION = "Project using CIFAR dataset."


import os
root_folder_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
ref_data = pd.read_csv(r"../data/ref_data.csv")
prod_data = pd.read_csv(r"../data/prod_data.csv")

label_ref_data = ref_data.copy(deep=True)
label_prod_data = prod_data.copy(deep=True)

model=joblib.load(open(r"../artifacts/best_model.pkl", 'rb'))

ref_data['prediction'] = model.predict(ref_data.iloc[:, :-1])
label_ref_data['prediction'] = ref_data['prediction']
label_prod_data['prediction'] = prod_data["prediction"]




def create_report(i: int):
    classification_report=Report(metrics=[
        ClassificationQualityMetric(),
        ClassificationClassBalance(),
        ClassificationConfusionMatrix(),
        ClassificationQualityByClass(),
        ClassificationDummyMetric(),
    ],
    timestamp=datetime.datetime.now() + datetime.timedelta(days=i),)

    classification_report.run(reference_data=label_ref_data, current_data=label_prod_data)
    return classification_report


def create_project(workspace: WorkspaceBase):
    project = workspace.create_project(YOUR_PROJECT_NAME)
    project.description = YOUR_PROJECT_DESCRIPTION
    project.dashboard.add_panel(
        DashboardPanelCounter(
            title="Share of Drifted Features",
            filter=ReportFilter(metadata_values={}, tag_values=[]),
            value=PanelValue(
                metric_id="DatasetDriftMetric",
                field_path="share_of_drifted_columns",
                legend="share",
            ),
            text="share",
            agg=CounterAgg.LAST,
            size=1,
        )
    )
    project.save()
    return project


def create_demo_project(workspace: str):
    ws = Workspace.create(workspace)
    project = create_project(ws)

    for i in range(0, 1):
        report = create_report(i=i)
        ws.add_report(project.id, report)
if __name__ == "__main__":
    create_demo_project(WORKSPACE)
