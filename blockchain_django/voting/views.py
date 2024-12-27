# voting/views.py
from django.shortcuts import render, redirect
from .models import Candidate
from .forms import CandidateForm
from .blockchain import Blockchain  # Import the blockchain logic

# Initialize the blockchain (you can do this globally if needed)
blockchain = Blockchain()

def create_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()  # Save the candidate to the database
            return redirect('candidate_list')  # Redirect to candidate list
    else:
        form = CandidateForm()
    return render(request, 'voting/create_candidate.html', {'form': form})

def candidate_list(request):
    candidates = Candidate.objects.all()  # Get all candidates from the database
    return render(request, 'voting/candidate_list.html', {'candidates': candidates})

def vote_candidate(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    
    # Update the votes for the candidate in the database
    candidate.votes += 1
    candidate.save()

    # Add the voting transaction to the blockchain
    # Let's assume a simple voting system where user IP is used as sender
    blockchain.new_transaction(
        sender=request.META.get('REMOTE_ADDR'),  # User IP as sender
        recipient=candidate.name,  # Candidate name as recipient
        amount=1,  # Vote is considered 1 unit
    )

    # Once the transaction is added, mine the new block
    blockchain.new_block(proof=100)  # Add proof as part of the block

    return redirect('candidate_list')  # Redirect to the list of candidates

def blockchain_view(request):
    # You can add other details you need to show
    chain = blockchain.chain
    return render(request, 'voting/blockchain_view.html', {'chain': chain})
