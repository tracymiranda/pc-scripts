#!/usr/bin/env python

import os, sys, argparse
from report import *
from show_report import *

def custom_filter(S):
    S = S.filter(lambda s: s.average >= 3.7 or '+p' in s.tags)
    S = S.filter(lambda s: not '+n' in s.tags)
    S = S.filter(lambda s: not '+C' in s.tags)
    S = S.filter(lambda s: not s.accepted)

    # Half talks
    # S = S.filter(lambda s: "half" in s.tags or "+C" in s.tags)
    # S = S.filter(lambda s: "+n" in s.tags)
    # S = S.filter(lambda s: "+p" in s.tags)

    return S

def add_custom_command(subparsers):
    def run(S, args):
        G = custom_filter(S)
        ids = map(lambda s: s.id, G.subs)
        not_lost = set([])
        lost = set([])
        for s in S.subs:
            is_lost = not s.id in ids
            if args.info_type == "tags":
                if is_lost:
                    lost.update(s.tags)
                else:
                    not_lost.update(s.tags)
            elif args.info_type == "projects":
                if is_lost:
                    lost.update(s.projects)
                else:
                    not_lost.update(s.projects)
            elif args.info_type == "companies":
                if is_lost:
                    lost.add(s.company)
                else:
                    not_lost.add(s.company)
            else:
                raise Exception("Unknown aggregate info, should be one of (tags/projects/companies)")


        for l in sorted(lost.difference(not_lost)):
            if l:
                print l

    parser_custom = subparsers.add_parser("custom")
    parser_custom.add_argument('info_type', metavar='INFO_TYPE', help='tags, projects, or companies')
    parser_custom.set_defaults(func=run)


def print_subs(S):
    S.print_subs()

def print_summary(S, min_vote):
    show_report(S, min_vote=min_vote)

def filter_min_vote_count(S, min_vote_count):
    return S.filter(lambda s: s.count >= min_vote_count)

def filter_min_vote(S, min_vote):
    return S.filter(lambda s: s.average >= min_vote)

def filter_max_vote(S, max_vote):
    return S.filter(lambda s: s.average < max_vote)

def add_all_command(subparsers):
    def run(S, args):
        return S
    parser_all = subparsers.add_parser("all")
    parser_all.set_defaults(func=run)

def add_tag_command(subparsers):
    def run(S, args):
        tags = args.tags
        merged = Submissions([])
        for tag in tags:
            merged = merged.union(S.find_tag(tag))
        return merged
    parser_tag = subparsers.add_parser("tag")
    parser_tag.add_argument('tags', metavar='TAGS', nargs='+',
                   help='Tags to query')
    parser_tag.set_defaults(func=run)

def add_tags_command(subparsers):
    def run(S, args):
        print "Tag          \t\tSubmission Count"

        for (tag, count) in sorted(S.tag_count().items(), key=lambda (x, _): x):
            if tag:
                print "%s\t\t%s" % (tag.ljust(20), count)

    parser_tags = subparsers.add_parser("tags")
    parser_tags.set_defaults(func=run)

def add_project_command(subparsers):
    def run(S, args):
        projects = args.projects
        merged = Submissions([])
        for project in projects:
            merged = merged.union(S.find_project(project))
        return merged
    parser_project = subparsers.add_parser("project")
    parser_project.add_argument('projects', metavar='PROJECTS', nargs='+',
                   help='Projects to query')
    parser_project.set_defaults(func=run)

def add_projects_command(subparsers):
    def run(S, args):
        print "Project      \t\tSubmission Count"

        for (project, count) in S.project_count().items():
            if project:
                print "%s\t\t%s" % (project.ljust(20), count)

    parser_project = subparsers.add_parser("projects")
    parser_project.set_defaults(func=run)

def add_language_command(subparsers):
    def run(S, args):
        languages = args.languages
        merged = Submissions([])
        for language in languages:
            merged = merged.union(S.find_language(language))
        return merged
    parser_language = subparsers.add_parser("language")
    parser_language.add_argument('languages', metavar='LANGUAGES', nargs='+',
                   help='Languages to query')
    parser_language.set_defaults(func=run)

def add_languages_command(subparsers):
    def run(S, args):
        print "Language      \t\tSubmission Count"

        for (language, count) in S.language_count().items():
            if language:
                print "%s\t\t%s" % (language.ljust(20), count)

    parser_language = subparsers.add_parser("languages")
    parser_language.set_defaults(func=run)

def add_track_command(subparsers):
    def run(S, args):
        tracks = args.tracks
        merged = Submissions([])
        for track in tracks:
            merged = merged.union(S.find_track(track))
        return merged
    parser_track = subparsers.add_parser("track")
    parser_track.add_argument('tracks', metavar='TRACKS', nargs='+',
                   help='Tracks to query')
    parser_track.set_defaults(func=run)

def add_tracks_command(subparsers):
    def run(S, args):
        print "Track      \t\tSubmission Count"

        for (track, count) in S.track_count().items():
            if track:
                print "%s\t\t%s" % (track.ljust(20), count)

    parser_track = subparsers.add_parser("tracks")
    parser_track.set_defaults(func=run)

def add_company_command(subparsers):
    def run(S, args):
        companys = args.companys
        merged = Submissions([])
        for company in companys:
            merged = merged.union(S.find_company(company))
        return merged
    parser_company = subparsers.add_parser("company")
    parser_company.add_argument('companys', metavar='COMPANYS', nargs='+',
                   help='Companys to query')
    parser_company.set_defaults(func=run)

def add_companies_command(subparsers):
    def run(S, args):
        print "Company Count\t\tSubmission Count"

        for (company, count) in S.company_count().items():
            if company:
                print "%s\t\t%s" % (company.ljust(20), count)

    parser_company = subparsers.add_parser("companies")
    parser_company.set_defaults(func=run)

def add_speaker_command(subparsers):
    def run(S, args):
        speakers = args.speakers
        merged = Submissions([])
        for speaker in speakers:
            merged = merged.union(S.find_speaker(speaker))
        return merged
    parser_speaker = subparsers.add_parser("speaker")
    parser_speaker.add_argument('speakers', metavar='SPEAKERS', nargs='+',
                   help='Speakers to query')
    parser_speaker.set_defaults(func=run)

def add_speakers_command(subparsers):
    def run(S, args):
        print "Speaker Count\t\tSubmission Count"

        for (speaker, count) in S.speaker_count().items():
            if speaker and count > 1:
                print "%s\t\t%s" % (speaker.ljust(20), count)

    parser_speaker = subparsers.add_parser("speakers")
    parser_speaker.set_defaults(func=run)

def add_id_command(subparsers):
    def run(S, args):
        return S.filter(lambda s: s.id in args.ids)
    parser_speaker = subparsers.add_parser("id")
    parser_speaker.add_argument('ids', metavar='IDS', nargs='+',
                   help='List of node ids to include')
    parser_speaker.set_defaults(func=run)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Filters
    parser.add_argument('-m', "--min", type=float, default=os.environ.get('FOSS4G_MIN_VOTE', 0.0), help="Minimum vote to consider (inclusive)")
    parser.add_argument('-M', "--max", type=float, default=5.1, help="Maximum vote to consider (non-inclusive)")
    parser.add_argument('-v', "--votecount", type=int, default=0, help="Minimum vote count from PC to consider.")

    # Actions
    parser.add_argument('-x', "--accepted", action='store_true')
    parser.add_argument('-o', "--open", action='store_true')
    parser.add_argument('-s', "--save", default="")
    parser.add_argument('-f', "--force", action='store_true')
    parser.add_argument('-a', "--all", action='store_true', help="Print each individual submission results (default for under 10 results).")
    parser.add_argument('-r', "--report", action='store_true', help="Print summary report (default for 10 or more results).")
    parser.add_argument('-t', "--tutorials", action='store_true', help="Show tutorials instead of standard talks.")
    parser.add_argument('-p', "--poc", action='store_true', help="Filter for isPOC.")
    parser.add_argument('-w', "--woman", action='store_true', help="Filter for isWoman.")
    parser.add_argument("--custom", action='store_true', help="Custom filter.")

    subparsers = parser.add_subparsers()

    # Add subparsers
    add_all_command(subparsers)
    add_custom_command(subparsers)
    add_tag_command(subparsers)
    add_tags_command(subparsers)
    add_project_command(subparsers)
    add_projects_command(subparsers)
    add_language_command(subparsers)
    add_languages_command(subparsers)
    add_track_command(subparsers)
    add_tracks_command(subparsers)
    add_company_command(subparsers)
    add_companies_command(subparsers)
    add_speaker_command(subparsers)
    add_speakers_command(subparsers)
    add_id_command(subparsers)

    args = parser.parse_args()

    # Filter submissions
    S = ALL
    if args.tutorials:
        S = S.tutorials()
    else:
        S = S.standard()

    if args.custom:
        S = custom_filter(S)
    else:
        S = filter_min_vote_count(S, args.votecount)
        S = filter_min_vote(S, args.min)
        S = filter_max_vote(S, args.max)

    if args.poc:
        S = S.filter(lambda x: x.isPOC)

    if args.woman:
        S = S.filter(lambda x: x.isWoman)

    if args.accepted:
        S = S.filter(lambda s: s.accepted)

    # Execute query type
    S = args.func(S, args)

    print map(lambda x: x.id, S.subs)

    # If we returned results, potentially do things to them
    if S:
        # Perform any actions
        if args.all or (len(S.subs) < 10 and not args.report):
            print_subs(S)
        else:
            print_summary(S, args.min)

        if args.save:
            S.save_subs(args.save)

        if args.open:
            S.open_links(args.force)
