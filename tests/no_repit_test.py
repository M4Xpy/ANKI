from Source.srt_player_2.en_two_line import no_repit


class Test:

    class Test_no_repit111:

        def test_no_repit(self) -> None:
            assert no_repit('(ENGINE REVVING)', test=True) == ('(engine revving)', '(ENGINE REVVING)', False)

        def test_no_repit_1(self) -> None:
            assert no_repit('WOMAN: Come here, puppy.', test=True) == ('WOMAN: COME HERE, puppy.', ' puppy.', True)

        def test_no_repit_2(self) -> None:
            assert no_repit('(MEWS) (YELPS)', test=True) == ('(mews) (yelps)', '(MEWS) (YELPS)', False)

        def test_no_repit_colons(self) -> None:
            assert no_repit('7:00 a.m. Up and at \'em!', test=True) == ("7:00 A.M. UP AND AT 'EM!", '', False)

        def test_no_repit_dot(self) -> None:
            assert no_repit("- I'm on my knees for life. - I have no money to give you.", test=True) == (
                    "- I'm on my knees for life. - I HAVE NO MONEY TO GIVE YOU.", "- I'm on my knees for life.", True)

        def test_no_repit_doubles(self) -> None:
            assert no_repit('no, no, no.', test=True) == ('NO,', '', False)

        def test_no_repit_mr_dot(self) -> None:
            assert no_repit('-Mr. Gibbs. -Captain.', test=True) == ('-MR GIBBS. -CAPTAIN.', '', False)

        def test_no_repit_aphostroph(self) -> None:
            assert no_repit("Okay, well, I'm sorry. I, uh. . . .", test=True) == ("OKAY, WELL, I'M SORRY. UH.", '', False)

        def test_no_repit_schedule(self) -> None:
            assert no_repit('She just moved from L.A. to Salt Lake, so. . . .', test=True) == (
                    'She just moved from L.A. to Salt Lake, SO.', 'She just moved from L.A. to Salt Lake,', True)

        def test_no_repit_brace(self) -> None:
            assert no_repit('[SOFTLY] Jesus , (work)', test=True) == ('[softly] JESUS , (WORK)', '[SOFTLY]', True)

        def test_no_repit_mmhmm(self) -> None:
            assert no_repit('Do you like scary movies ? Mm-hmm.', test=True) == (
                    'Do you like scary movies ? MM-HMM.', 'Do you like scary movies ?', True)

        def test_no_repit_2000(self) -> None:
            assert no_repit("I'm sorry, 12-34-54", test=True) == ("I'M  SORRY,  12-34-54", '', False)

        def test_no_repit_dash(self) -> None:
            assert no_repit('no-no-no-no', test=True) == ()

        # def test_no_repit_schedule(self) -> None:
        #     assert no_repit('', test=True) == ()
