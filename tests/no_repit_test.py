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
            assert no_repit('7:00 a.m. Up and at \'em!') == ("7:00 a. Up and at 'em!", " Up and at 'em!", 1)

        def test_no_repit_dot(self) -> None:
            assert no_repit("- I'm on my knees for life. - I have no money to give you.") == (
            "- I'm on my knees for life. - I have no money to give you.",
            "- I'm on my knees for life. - I have no money to give you.", False)

        def test_no_repit_doubles(self) -> None:
            assert no_repit('no, no, no.') == ('no,', '', 0)


        def test_no_repit_mr_dot(self) -> None:
            assert no_repit('-Mr. Gibbs. -Captain.') == ('-Mr Gibbs. -Captain.', '-Mr Gibbs.', 1)

        def test_no_repit_aphostroph(self) -> None:
            assert no_repit("Okay, well, I'm sorry. I, uh. . . .") == ("Okay, well, I'm sorry. uh.", '', 0)

        # def test_no_repit_schedule(self) -> None:
        #     assert no_repit('') ==


