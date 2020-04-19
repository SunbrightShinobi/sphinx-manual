import os
import git

################################################################################
# Setup CM Status
################################################################################
#useGit = False
#dirty_build = False

def is_in_git():
    '''
    Tests if folder is part of a Git repo by returning True or False
    '''
    try:
        git.Repo(search_parent_directories=True)
    except git.exc.InvalidGitRepositoryError:
        return False
    return True

def get_git_reponame():
    '''
    Returns a string identifying the git repository's HEAD, useful for
    identifying the "release" of a build. If HEAD is tagged, returns the
    tag. Otherwise, returns the first 11 characters of the commit ID.
    Equivalent to the following shell code:
    if git describe --tags --dirty --exact-match &> /dev/null
    then
        git describe --tags --dirty --exact-match
    else
        git rev-parse --short=11 HEAD
    fi
    '''
    git_repo = git.Repo(search_parent_directories=True)

    try:
        return git_repo.remotes[0].url.split('/')[-1].split('.git')[0]
    except IndexError:
        return ''

def get_git_status():
    '''
    Gets the Git status of the build repository

    Args:
        None

    Returns:
        str: A string consisting of the git repository name, active
             branch name, and first 11 characters of commit hash, with
             ``(dirty)`` appended if local modifications are present.
    '''
    if not is_in_git():
        return [-1, 'Not in CM']
    git_repo = git.Repo(search_parent_directories=True)
    git_sha_full = git_repo.head.commit.hexsha
    git_sha = git_sha_full[:11]
    git_repo_name = get_git_reponame()
    try:
        active_branch = git_repo.active_branch.name
    except:
        active_branch = ''
        return ' '.join([git_sha, 
                         '(dirty)' if git_repo.is_dirty() else '',])
    return ' '.join(['Git:', 
                     git_repo_name.replace('_',r'\_'), 
                     '-', 
                     active_branch.replace('_',r'\_'), 
                     '(dirty)' if git_repo.is_dirty() else '', 
                     '[',
                     git_sha,
                     ']',
                     ])

def get_git_release():
    repo = git.Repo(search_parent_directories=True)
    try:
        tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
        if tags: 
            last_tag = tags[-1].tag
            if last_tag.object == repo.head.object:
                return last_tag.tag
            else:
                return repo.head.commit.hexsha[:11]
        else:
            return repo.head.commit.hexsha[:11]
    except AttributeError:
        '''
        If it's a lightweight tag, last_tag will be a None object.
        Annotated tags are instances of git.objects.tag.TagObject.
        We shouldn't be using lightweight tags for releases, so
        we'll just ignore the tag and use the commit ID.
        '''
        return repo.head.commit.hexsha[:11]

if is_in_git():
    release = get_git_status()
    if get_git_reponame():
        git_repo = get_git_reponame()
    else:
        git_repo = 'No Remote'
    gitstatus = 'inGit'
    gittag = get_git_release()
else:
    release='Non-CM'
    git_repo = 'None'
    gitstatus = 'not'
    gittag = 'draft'
