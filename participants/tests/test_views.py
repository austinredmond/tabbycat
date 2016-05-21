from utils.views_tests import PublicTableViewTest
from participants.models import Speaker, Adjudicator


class PublicParticipantsViewTestCase(PublicTableViewTest):

    view_toggle = 'public_features__public_participants'
    public_view_name = 'public_participants'

    def validate_table_data_a(self):
        # Check number of adjs matches
        return Adjudicator.objects.filter(tournament=self.t).count()

    def validate_table_data_b(self):
        # Check number of speakers matches
        return Speaker.objects.filter(team__tournament=self.t).count()
