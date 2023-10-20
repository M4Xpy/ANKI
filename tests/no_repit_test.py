from Source.srt_player_2.three_line_online_player import no_repit


class Test:

    class Test_no_repit111:

        def test_no_repit(self) -> None:
            assert no_repit('(ENGINE REVVING)') == ('(ENGINE REVVING)', '(ENGINE REVVING)', 0)

        def test_no_repit_1(self) -> None:
            assert no_repit('WOMAN: Come here, puppy.') == ('WOMAN: Come here, puppy.', ' puppy.', 1)

        def test_no_repit_2(self) -> None:
            assert no_repit('(MEWS) (YELPS)') == ('(MEWS) (YELPS)', '(MEWS) (YELPS)', 0)

        def test_no_repit_colons(self) -> None:
            assert no_repit('7:00 a.m. Up and at \'em!') == ("7:00 a.m. Up and at 'em!", '', 0)

        def test_no_repit_dot(self) -> None:
            assert no_repit("- I'm on my knees for life. - I have no money to give you.") == (
                    "- I'm on my knees for life. - I have no money to give you.", "- I'm on my knees for life.", 1)

        def test_no_repit_doubles(self) -> None:
            assert no_repit('no, no, no.') == ('no,', '', 0)

        def test_no_repit_mr_dot(self) -> None:
            assert no_repit('-Mr. Gibbs. -Captain.') == ('-Mr Gibbs. -Captain.', '', 0)

        def test_no_repit_aphostroph(self) -> None:
            assert no_repit("Okay, well, I'm sorry. I, uh. . . .") == ("Okay, well, I'm sorry. uh.", '', 0)

        def test_no_repit_schedule(self) -> None:
            assert no_repit('She just moved from L.A. to Salt Lake, so. . . .') == (
            'She just moved from L.A. to Salt Lake, so.', 'She just moved from L.A. to Salt Lake,', 1)

        def test_no_repit_brace(self) -> None:
            assert no_repit('[SOFTLY] Jesus , (work)') == ('[SOFTLY] Jesus , (work)', '[SOFTLY]', 1)

        def test_no_repit_mmhmm(self) -> None:
            assert no_repit('Do you like scary movies ? Mm-hmm.') == (
                    'Do you like scary movies ? Mm-hmm.', 'Do you like scary movies ?', 1)

        # def test_no_repit_2000(self) -> None:
        #     assert no_repit('Okay. Mmm-hmm.') == ()

        # def test_no_repit_schedule(self) -> None:
        #     assert no_repit('') == ()


